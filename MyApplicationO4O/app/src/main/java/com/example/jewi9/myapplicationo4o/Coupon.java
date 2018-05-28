package com.example.jewi9.myapplicationo4o;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;

public class Coupon extends AppCompatActivity {
    private ArrayList<HashMap<String,String>> Data = new ArrayList<HashMap<String, String>>();
    private ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.couponlist);

        listView =(ListView)findViewById(R.id.List_view);
        JSONObject coupon1 = new JSONObject();
        JSONObject coupon2 = new JSONObject();

        /*JSONArray couponArray = new JSONArray();//jsonArray형태로 서버에서 쿠폰정보를 받아올것임.
        try {
            coupon1.accumulate("name","coupon1");
            coupon1.accumulate("dueDate","2018-5-26");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        try {
            coupon2.accumulate("name","coupon2");
            coupon2.accumulate("dueDate","2018-5-30");
        } catch (JSONException e) {
            e.printStackTrace();
        }
        couponArray.put(coupon1);
        couponArray.put(coupon2);*/
        Menu menu = new Menu();
        //Menu.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        for(int i=0;i<menu.couponArray.length();i++){
            try {
                 HashMap<String,String> InputData1 = new HashMap<>();

                InputData1.put("name", menu.couponArray.getJSONObject(i).getString("name"));
                InputData1.put("dueDate",menu.couponArray.getJSONObject(i).getString("dueDate"));
                Data.add(InputData1);

            } catch (JSONException e) {
                e.printStackTrace();
            }

        }
        /*adapter생성*/
        SimpleAdapter simpleAdapter = new SimpleAdapter(this,Data,android.R.layout.simple_list_item_2,new String[]{"name","dueDate"},new int[]{android.R.id.text1,android.R.id.text2});
        listView.setAdapter(simpleAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Intent intent = new Intent(getApplicationContext(),ClickCoupon.class);
                startActivity(intent);
            }
        });
    }
}
